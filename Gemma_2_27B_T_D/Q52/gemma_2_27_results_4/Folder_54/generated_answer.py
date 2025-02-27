def palindrome_of_length_n(string):
    return {s for s in [string[i:i + 85].lower() for i in range(len(string) - 84)] if s == s[::-1] and s.isalpha()}