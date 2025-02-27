def palindromes_of_specific_lengths(text):
    r = '^[a-z]+$'
    ans = set()
    for i in range(40, 95):
        for j in range(i + 45, i + 52):
            pal = text[i:j + 1] if text[i:j + 1] else None
            if pal and re.match(r, pal.lower()):
                ans.add(pal)
    return ans