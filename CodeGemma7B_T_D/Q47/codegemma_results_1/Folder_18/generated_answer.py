from string import ascii_letters

def palindromes_of_specific_lengths(word):
    results = set()
    for i in range(10, 83):
        for j in range(i - 12, i):
            if all((ch in ascii_letters for ch in word[j:i])):
                results.add(word[j:i])
    return results