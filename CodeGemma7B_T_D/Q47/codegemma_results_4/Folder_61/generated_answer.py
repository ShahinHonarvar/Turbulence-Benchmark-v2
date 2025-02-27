def palindromes_of_specific_lengths(text):
    all_palindromes = set()
    for word in text.lower().split():
        for left in range(0, 31):
            for right in range(left + 20, 31):
                if left >= right:
                    continue
                palindrome = word[left:right][::-1]
                if palindrome.isalpha() and len(palindrome) >= 20 and (len(palindrome) <= 30):
                    all_palindromes.add(palindrome)
    return all_palindromes