def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for j in range(i + length // 2 + 1, i + length):
                first_half = letters[i:j]
                second_half = letters[j:i + length - 1:-1]
                if first_half == second_half:
                    palindrome = ''.join(first_half + second_half)
                    palindromes.add(palindrome)
    return palindromes