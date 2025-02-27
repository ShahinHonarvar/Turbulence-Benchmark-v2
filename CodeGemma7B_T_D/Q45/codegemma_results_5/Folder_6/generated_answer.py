from itertools import permutations

def palindromes_between_indices(s):
    lower_s = s.lower()
    letters = lower_s[0:8]
    count = {letter: lower_s.count(letter) for letter in letters}
    if any(count.values()) == 0:
        return set()
    palindromes = set()
    for p in permutations(letters):
        first = ''.join(p[0:4])
        mid = ''.join(p[4:5])
        last = ''.join(p[5:9])
        if first == first[::-1] and mid == mid[::-1] and (last == last[::-1]):
            palindrome = first + mid + last
            palindromes.add(palindrome)
    return palindromes