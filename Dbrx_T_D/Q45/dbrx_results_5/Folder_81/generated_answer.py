from functools import reduce

def is_palindrome(word):
    return word == word[::-1]

def partition(string, start, end):
    if start == end:
        return [[string[start]]]
    result = []
    for k in range(start, end + 1):
        for partition in partition(string, start, k):
            for suffix in partition(string, k + 1, end):
                result.append(partition + [string[k]] + suffix)
    return list(filter(lambda partition: is_palindrome(reduce(lambda x, y: x + y, partition)), result))

def palindromes_between_indices(string):
    partitions = partition(string.lower(), 0, 6)
    return {reduce(lambda x, y: x + y, partition) for partition in partitions if len(partition) >= 3}