from string import ascii_letters

def palindrome_of_length_n(s: str):
    return {sub[i:i + 40] for sub in s + s.lower() for i in range(len(sub) - 40 + 1) if sub[i:i + 40].isalpha()}