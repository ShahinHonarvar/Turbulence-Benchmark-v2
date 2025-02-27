def palindromes_between_indices(s):
    s = s[:5].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    if len(letters) < 3:
        return palindromes
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters) + 1):
                for first_half in generate_permutations(letters[:i] + letters[j:k]):
                    for last_half in generate_permutations(letters[j:i] + letters[k:]):
                        if len(first_half) == len(last_half):
                            palindrome = first_half + ''.join(reversed(last_half))
                            if len(palindrome) >= 3:
                                palindromes.add(palindrome)
    return palindromes

def generate_permutations(chars):
    if len(chars) == 1:
        return [chars]
    permutations = set()
    for i in range(len(chars)):
        char = chars[i]
        rest = chars[:i] + chars[i + 1:]
        for p in generate_permutations(rest):
            permutations.add(char + p)
    return permutations