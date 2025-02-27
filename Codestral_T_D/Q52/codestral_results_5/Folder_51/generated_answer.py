def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 73] for i in range(len(s) - 72) if s[i:i + 73] == s[i:i + 73][::-1] and s[i:i + 73].isalpha()}