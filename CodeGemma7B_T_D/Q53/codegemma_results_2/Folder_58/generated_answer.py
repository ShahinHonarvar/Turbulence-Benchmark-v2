def palindrome_of_length_at_least_n(text):
    words = text.lower().split()
    palindrome_set = set()
    for word in words:
        if len(word) >= 147 and word == word[::-1]:
            palindrome_set.add(word)
    return palindrome_set