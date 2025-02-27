import re
from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    """
    Finds all palindromes of length greater than or equal to 85 in a string.

    Args:
        text: The string to search for palindromes in.

    Returns:
        A set of all palindromes of length greater than or equal to 85, or an empty set if no such palindromes exist.
    """
    text = re.sub('[^a-zA-Z]', '', text.lower())
    counts = defaultdict(int)
    for char in text:
        counts[char] += 1
    palindromes = set()
    for start, mid in enumerate(text):
        for end in range(start + 85, len(text) + 1):
            if all((count % 2 == 0 for count in counts.values())):
                palindromes.add(text[start:end])
    return palindromes