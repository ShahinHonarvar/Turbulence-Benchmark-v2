import itertools

def palindromes_between_indices(s):
    s = s[2:10].lower()
    char_count = {}
    for char in s:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    odd_chars = [char for char, count in char_count.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    palindromes = set()
    half_part = []
    for char, count in sorted(char_count.items()):
        half_part.append(char * (count // 2))
    half_part = ''.join(half_part)
    permutations = set(itertools.permutations(half_part))
    center = ''
    if odd_chars:
        center = odd_chars[0]
    for perm in permutations:
        palindrome = ''.join(perm) + center + ''.join(perm[::-1])
        if len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes