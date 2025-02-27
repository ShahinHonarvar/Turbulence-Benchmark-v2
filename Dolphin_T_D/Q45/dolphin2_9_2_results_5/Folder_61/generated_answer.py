import itertools

def palindromes_between_indices(s):
    letters = [ch for ch in s[:8] if ch.isalpha()]
    palindromes = set()
    for p in range(7, len(letters) + 1):
        for combination in itertools.permutations(letters, p):
            for palindrome in itertools.product(*[itertools.combinations_with_replacement(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], p)]):
                if ''.join(palindrome) == ''.join(palindrome)[::-1]:
                    palindromes.add(''.join(palindrome))
    return palindromes