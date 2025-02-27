import itertools

def palindromes_between_indices(s):
    s = s[7:10].lower()
    letters = set(s)
    result = set()
    for r in range(4, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            first_half = ''.join(combo[:r // 2])
            if r % 2 == 0:
                palindrome = first_half + first_half[::-1]
            else:
                palindrome = first_half + combo[r // 2] + first_half[::-1]
            result.add(palindrome)
            if len(combo) > 2 and r % 2 == 1:
                first_half = ''.join(combo[:r // 2 + 1])
                palindrome = first_half + first_half[::-1]
                result.add(palindrome)
    return result