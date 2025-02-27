def palindromes_between_indices(s):
    chars = ''.join(sorted(set(s[3:9])))
    length = len(chars)

    def helper(pal, length, i):
        if i >= length:
            if pal == pal[::-1]:
                if len(pal) >= 5:
                    yield pal
            return
        for c in chars[i:]:
            helper(pal + c, length, i + 1)
    return set(helper('', length, 0))