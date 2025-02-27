import re

def palindromes_of_specific_lengths(string):
    pattern = re.compile('(?i)(?<=^.{119})([a-z]{104,123}\\\\b)(?=.{135})$')

    def reverse_string(text):
        return text[::-1]
    palindromes = set()
    for match in re.finditer(pattern, string):
        for i in range(match.start(), match.end() - match.span()[1] + 1):
            if string[i] not in 'abcdefghijklmnopqrstuvwxyz':
                continue
            left, right = (i, match.end() + i - 1)
            while left < right and string[left] == reverse_string(string[right])[0]:
                left += 1
                right -= 1
            if left >= right:
                palindromes.add(string[i:match.end() + i + 1])
    return palindromes