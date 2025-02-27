def palindromes_between_indices(text):
    low, high = (ord('a'), ord('z'))
    seen = set()
    palindromes = set()
    for c in text[3:6].lower():
        if low <= ord(c) <= high:
            seen.add(c)
    if not seen:
        return palindromes
    for c in text[3:6].lower():
        for i in range(c, high + 1):
            if chr(i) in seen:
                seen.remove(chr(i))
            else:
                continue
            for j in range(i, low - 1, -1):
                if chr(j) in seen:
                    seen.remove(chr(j))
                else:
                    continue
                palindromes.add(''.join(sorted([chr(i)] + list(seen) + [chr(j)])))
    return palindromes