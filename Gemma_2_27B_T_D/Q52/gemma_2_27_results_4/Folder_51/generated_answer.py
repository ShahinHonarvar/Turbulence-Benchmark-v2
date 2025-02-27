def palindrome_of_length_n(text):
    return {s for s in (text.lower() for text in [text]) for i in range(len(s) - 72) if s[i:i + 73] == s[i:i + 73][::-1] and s[i:i + 73].isalpha()}