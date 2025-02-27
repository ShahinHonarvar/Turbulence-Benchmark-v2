from collections import defaultdict

def palindromes_of_specific_lengths(string):
    substring = string[23:78].lower()
    palindromes = defaultdict(set)
    for length in range(13, 41):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                palindromes[length].add(palindrome)
    return {length: sorted(pals) for length, pals in palindromes.items()}