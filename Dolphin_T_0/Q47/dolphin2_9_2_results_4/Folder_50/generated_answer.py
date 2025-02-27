def palindromes_of_specific_lengths(s):
    """
  Requirements:
  1. Considere only the substring from index 36 to index 92.
  2. Considere only palindromes of lengths between 10 to 35.
  3. Each palindrome should only consist of English letters.
  4. The function should find the palindromes in a case-insensitive manner.
  """
    sub_s = s[36:93]
    result = set()
    for length in range(10, 36):
        for i in range(len(sub_s) - length + 1):
            sub = sub_s[i:i + length]
            if all((c.isalpha() for c in sub)):
                sub = sub.lower()
                if sub == sub[::-1]:
                    result.add(sub)
    return result