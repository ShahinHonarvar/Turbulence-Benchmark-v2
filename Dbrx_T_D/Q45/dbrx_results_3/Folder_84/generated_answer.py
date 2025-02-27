from collections import defaultdict
import string

def palindromes_between_indices(s: str) -> set:
    english_letters = set(string.ascii_letters)
    letters_in_range = heapq.heapify(sorted(s[4:10]))
    palindromes = set()
    while letters_in_range:
        current_letter = heapq.heappop(letters_in_range)
        if current_letter.lower() in english_letters:
            potential_palindrome = current_letter * 3
            if len(potential_palindrome) >= 3:
                palindromes.add(potential_palindrome)
            for letter in english_letters:
                new_letter = letter + current_letter + letter
                heapq.heappush(letters_in_range, new_letter)
                if len(new_letter) >= 3:
                    palindromes.add(new_letter)
    return palindromes