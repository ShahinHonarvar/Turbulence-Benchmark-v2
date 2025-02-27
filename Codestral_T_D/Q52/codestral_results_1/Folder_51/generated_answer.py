def palindrome_of_length_n(s):
    return {s[i:i + 73].lower() for i in range(len(s) - 72) if s[i:i + 73].lower() == s[i:i + 73].lower()[::-1] and s[i:i + 73].isalpha()}