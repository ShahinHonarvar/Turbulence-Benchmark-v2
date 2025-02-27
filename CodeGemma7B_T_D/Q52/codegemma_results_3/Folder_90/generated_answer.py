from itertools import combinations

def palindrome_of_length_n(word):
    word = word.lower()
    result = set()
    for i in range(len(word) - 2):
        for j in range(i + 1, len(word) - 1):
            for k in range(j + 1, len(word)):
                substring = word[i:k + 1]
                if substring == substring[::-1]:
                    result.add(substring)
    return result