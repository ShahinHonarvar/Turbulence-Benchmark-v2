from collections import defaultdict

def palindrome_of_length_n(word):
    word = word.lower()
    strings = defaultdict(list)
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            strings[j - i].append(word[i:j])
    palindromes = set()
    for length, string in strings.items():
        if length == 35:
            for word in string:
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes