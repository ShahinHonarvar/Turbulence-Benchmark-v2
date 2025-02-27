def palindrome_of_length_at_least_n(text):
    return {s for s in text.lower() for i in range(len(s)) if len(s) >= 93 and s[i:i + len(s) // 2] == s[i + len(s) // 2:][::-1]}