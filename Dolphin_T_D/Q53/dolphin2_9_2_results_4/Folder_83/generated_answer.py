def palindrome_of_length_at_least_n(s):
    result = set()
    words = s.lower().split()
    for word in words:
        if len(word) >= 60:
            if word == ''.join(reversed(word)):
                if word.isalpha():
                    result.add(word)
    return result