import re
    from collections import Counter

def palindromes_between_indices(string):
    string = string[4:9]
    string = ''.join(re.findall('[a-zA-Z]+', string))
    result = set()
    for i in range(5, len(string) + 1):
        for j in range(len(string) - i + 1):
            substring = string[j:j + i]
            if len(substring) >= 5:
                substring_lower = substring.lower()
                is_palindrome = True
                counts = Counter(substring_lower)
                odd_counts = 0
                for char, count in counts.items():
                    if count % 2 != 0:
                        odd_counts += 1
                if odd_counts > 1:
                    is_palindrome = False
                if is_palindrome and substring_lower[::-1] == substring_lower:
                    result.add(substring_lower)
    return result