from collections import defaultdict

def palindromes_between_indices(s):

    def extend_palin(k, start, end):
        while start >= 0 and end < len(s) and (s[start].lower() == s[end].lower()):
            k.append(s[start])
            k = k[1:] + k[:1]
            start -= 1
            end += 1
        return k
    letters = defaultdict(int, {c: i for i, c in enumerate(s)})
    result = set()
    for i in range(4, 6):
        for c in range(min(letters.keys()), max(letters.keys()) + 1):
            if not letters[c]:
                continue
            k = [c]
            letters[c] -= 1
            left, right = (i - 1, i + 1)
            while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
                if s[left] == s[right]:
                    k = extend_palin(k, left - 1, right + 1)
                    result.add(''.join(k))
                    letters[s[left]] += 1
                    break
                left -= 1
                right += 1
            letters[c] += 1
    return result