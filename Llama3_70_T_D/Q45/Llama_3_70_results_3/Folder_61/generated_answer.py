import itertools

def palindromes_between_indices(s):
    letters = [char for char in s[:8].lower() if char.isalpha()]
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            first_half = ''.join(combo[:len(combo) // 2])
            second_half = ''.join(combo[len(combo) // 2:])[::-1]
            palindrome = first_half + second_half + first_half[::-1] if len(combo) % 2 == 0 else first_half + combo[len(combo) // 2] + first_half[::-1]
            palindromes.add(palindrome)
    return palindromes