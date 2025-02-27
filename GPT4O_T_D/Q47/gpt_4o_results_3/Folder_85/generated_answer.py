def palindromes_of_specific_lengths(s):
    start, end = (29, 98)
    s = s[start:end + 1]
    palindromes = set()
    for length in range(6, 10):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            cleaned_sub = ''.join(filter(str.isalpha, sub))
            if cleaned_sub.lower() == cleaned_sub[::-1].lower() and len(cleaned_sub) == length:
                palindromes.add(sub)
    return palindromes