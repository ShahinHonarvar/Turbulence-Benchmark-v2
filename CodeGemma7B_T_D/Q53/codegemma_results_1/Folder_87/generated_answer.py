def palindrome_of_length_at_least_n(txt):
    txt = txt.lower().replace(' ', '')
    return {txt[i:i + n] for n in range(18, len(txt) + 1) for i in range(len(txt) - n + 1) if txt[i:i + n] == txt[i:i + n][::-1]}