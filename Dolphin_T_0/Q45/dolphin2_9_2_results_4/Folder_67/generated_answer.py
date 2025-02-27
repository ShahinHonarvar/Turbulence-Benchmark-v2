from itertools import permutations, chain

def palindromes_between_indices(s):
    letters = s[2:7].lower()
    chars = set(letters)
    if len(chars.intersection(set('abcdefghijklmnopqrstuvwxyz'))) < 5:
        return set()
    palindromes_list = set()
    for length in range(5, len(letters) + 1):
        for subset in chain(permutations(chars, length), combinations_repeating(letters, length)):
            subset = ''.join(subset)
            for word in permutations(subset, length):
                word = ''.join(word)
                if word == word[::-1]:
                    palindromes_list.add(word)
    return palindromes_list

def combinations_repeating(elements, k):
    temp = [i for i in elements]
    for i in range(k - 1, 0, -1):
        if temp[i - 1] != temp[i]:
            temp[i - 1], temp[i] = (temp[i], temp[i - 1])
            yield ''.join(temp[:k])
            temp_copy = list(temp)
            i = k - 2
            while i >= 0 and temp_copy[i] == temp[i]:
                i -= 1
            while i >= 0:
                temp[i] = temp_copy[i]
                i -= 1

def permutations(elements, length):
    if length == 0:
        yield []
    else:
        for index, value in enumerate(elements):
            for permutation in permutations(elements, length - 1):
                yield ([value] + permutation)