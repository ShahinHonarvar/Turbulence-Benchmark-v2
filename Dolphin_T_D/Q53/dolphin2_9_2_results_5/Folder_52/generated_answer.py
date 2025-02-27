def palindrome_of_length_at_least_n(s):
    s = s.lower()
    words = set()
    for word in s.split():
        if len(word) >= 14:
            if word == word[::-1]:
                words.add(word)
    return words