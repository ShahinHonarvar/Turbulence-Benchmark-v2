def palindromes_between_indices(s):
    chars_between_indices = [c for c in s[1:9] if c.isalpha()]
    all_palindromes = set()
    for p in range(7, len(chars_between_indices) + 1):
        for subset in itertools.permutations(chars_between_indices, p):
            for palindrome in get_palindromes(subset, p):
                all_palindromes.add(palindrome)
    return all_palindromes

def get_palindromes(chars, length):
    palindromes = set()
    for i in range(len(chars)):
        for j in range(i + length, len(chars) + 1):
            if ''.join(chars[i:j]) == ''.join(chars[i:j][::-1]):
                palindromes.add(''.join(chars[i:j]).lower())
    return palindromes