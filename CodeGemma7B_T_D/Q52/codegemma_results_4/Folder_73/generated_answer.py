from string import ascii_lowercase

def palindrome_of_length_n(s):

    def generate_permutations(start, end):
        if start >= end:
            yield ''.join(p)
        else:
            for c in ascii_lowercase:
                if end - start >= len(c):
                    p[start] = c
                    yield from generate_permutations(start + 1, end)
    result = set()
    for i in range(len(s)):
        for j in range(i + 40, len(s) + 1):
            for p in generate_permutations(i, j):
                if p.lower() in s.lower():
                    result.add(p)
    return result