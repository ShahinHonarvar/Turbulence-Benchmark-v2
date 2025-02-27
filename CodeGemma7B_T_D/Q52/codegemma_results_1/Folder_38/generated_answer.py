def palindrome_of_length_n(str):
    return {s for s in str.lower() if len(s) == 38 and s == s[::-1]}