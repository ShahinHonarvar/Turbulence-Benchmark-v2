def palindromes_between_indices(text):
    result = set()
    for i in range(ord('a'), ord('z') + 1):
        for j in range(ord('a'), ord('z') + 1):
            for k in range(ord('a'), ord('z') + 1):
                for l in range(ord('a'), ord('z') + 1):
                    for m in range(ord('a'), ord('z') + 1):
                        s = chr(i) + chr(j) + chr(k) + chr(l) + chr(m)
                        if s[0] >= text[2] and s[-1] <= text[6]:
                            for _ in range(5):
                                result.add(''.join(sorted(s)))
                                s = s[1:] + s[0]
    return result