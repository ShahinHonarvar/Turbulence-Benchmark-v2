from collections import defaultdict

def palindrome_of_length_at_least_n(string):
    palindrome = defaultdict(set)
    temp_string = string.lower()
    for i in range(len(temp_string)):
        for j in range(i, -1, -1):
            word = temp_string[j:i + 1]
            if word == word[::-1] and len(word) >= 14:
                palindrome[word].add(word)
    return set(palindrome.values())