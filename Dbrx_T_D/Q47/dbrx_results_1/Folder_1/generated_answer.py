from collections import defaultdict

def palindromes_of_specific_lengths(s):
    if not isinstance(s, str):
        return 'The input must be a string.'
    if len(s) < 90:
        return set()
    subs = s[14:90].lower()
    palindromes = set()
    freq = defaultdict(int)
    for char in subs:
        freq[char] += 1
    for length in range(40, 73):
        for i in range(0, len(subs) - length + 1):
            sub = subs[i:i + length]
            if all((char.isalpha() for char in sub)):
                if all((freq[char] % 2 == 0 or freq[char] == length - 1 for char in set(sub))):
                    palindromes.add(sub)
    return palindromes