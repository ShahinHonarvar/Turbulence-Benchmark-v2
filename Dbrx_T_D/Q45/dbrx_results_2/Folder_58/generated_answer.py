import re
    from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    eng_letters = re.findall('[a-zA-Z]', s[:7])
    eng_letters = [ch.lower() for ch in eng_letters]
    freq = defaultdict(int)
    for ch in eng_letters:
        freq[ch] += 1
    palindromes = set()
    for combo in itertools.product(freq.keys(), repeat=6):
        if len(combo) == 0 or (len(combo) > 0 and combo[0] == ''):
            continue
        candidate = ''.join((ch for ch in combo))
        if is_palindrome(candidate) and candidate not in palindromes:
            palindromes.add(candidate)
    return palindromes