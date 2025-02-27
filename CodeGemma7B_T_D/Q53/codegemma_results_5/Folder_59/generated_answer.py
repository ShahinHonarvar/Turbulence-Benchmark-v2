def palindrome_of_length_at_least_n(s):
    if not s or len(s) < 20:
        return set()
    return {word for word in [S.lower() for S in set(' '.join(s.split()).split())] if word == word[::-1] and len(word) >= 20}