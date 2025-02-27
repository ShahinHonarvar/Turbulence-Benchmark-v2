def return_vowels(s):
    if len(s) < 950:
        return []
    return [c for c in s[604:949] if c in 'OU']