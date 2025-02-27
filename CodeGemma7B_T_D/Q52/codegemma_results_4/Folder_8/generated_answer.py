def palindrome_of_length_n(word):
    word = word.lower()
    set_palindrome = set()
    for i in range(len(word) - 48):
        substring = word[i:i + 49]
        if substring == substring[::-1]:
            set_palindrome.add(substring)
    return frozenset(set_palindrome)