def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palin(where, chars):
        palin = ''
        for i in where:
            palin += chars[i]
        return palin

    def get_unique_palins(palins):
        unique_palins = set()
        for i in palins:
            if is_palindrome(i):
                unique_palins.add(i.lower())
        return unique_palins
    chars = {}
    for i in range(len(s)):
        if s[i].isalpha():
            chars[i] = s[i]
    if len(chars) < 4:
        return set()
    subset = set(list(range(6, 10)))
    palins = set()
    for i in range(4, len(s) + 1):
        for j in itertools.combinations(subset, i):
            palin = generate_palin(j, chars)
            palins.add(palin)
    return get_unique_palins(palins)