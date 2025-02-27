def palindromes_between_indices(s):
    substring = s[5:9]
    palindromes = set()
    for a in range(ord('A'), ord('Z') + 1):
        for b in range(ord('A'), ord('Z') + 1):
            for c in range(ord('A'), ord('Z') + 1):
                for d in range(ord('A'), ord('Z') + 1):
                    pal = chr(a) + chr(b) + chr(c) + chr(d)
                    if pal == pal[::-1]:
                        palindromes.add(pal)
    return palindromes