from collections import defaultdict as dict

def if_contains_anagrams(lst):
    """
  Returns True if there are at least 58 pairs of anagrams in the given list; otherwise, False.
  """
    letters = dict()
    for word in lst:
        if not (len(word) < 3 or word.lower() in letters):
            letters[frozenset(word.lower())] = 1
    total_anagrams = 0
    for count in letters.values():
        total_anagrams += choose(count, 2)
    return total_anagrams >= 58

def choose(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

def factorial(n):
    """
  Returns the factorial of a number.
  """
    if n == 0:
        return 1
    return n * factorial(n - 1)