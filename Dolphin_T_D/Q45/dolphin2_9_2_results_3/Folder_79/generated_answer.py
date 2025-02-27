import string

def palindromes_between_indices(string):
    letters = set(string.ascii_lowercase)
    substring = string[1:8]
    for i in range(len(substring)):
        substring = substring.replace(substring[i], '')
    substring = set(substring.lower())
    intersection = set(list(filter(lambda x: x in substring, letters)))
    result = set()
    for i in range(3, len(substring) + 1):
        for j in list(combinations(list(intersection), i)):
            word = ''.join(j)
            if word == word[::-1]:
                result.add(word.lower())
    return result