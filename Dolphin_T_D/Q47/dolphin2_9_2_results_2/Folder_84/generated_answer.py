def palindromes_of_specific_lengths(s):
    s = s[23:78]
    palindromes = set()
    for size in range(13, 41):
        for start in range(0, len(s) - size + 1):
            sub = s[start:start + size]
            if sub.lower() == sub[::-1].lower():
                if all((char.isalpha() for char in sub)):
                    palindromes.add(sub)
    return palindromes