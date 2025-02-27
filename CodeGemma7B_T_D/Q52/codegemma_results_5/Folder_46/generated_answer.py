def palindrome_of_length_n(s):
    return {p for p in s.lower() if p * 464 in s.lower()}