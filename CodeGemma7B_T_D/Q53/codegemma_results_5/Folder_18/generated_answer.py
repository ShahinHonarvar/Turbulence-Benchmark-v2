def palindrome_of_length_at_least_n(word):
    palindrome = set()
    for word in word.lower():
        if len(word) >= 62:
            palindrome.add(word)
    return palindrome