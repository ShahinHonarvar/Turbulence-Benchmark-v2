import re

def palindromes_of_specific_lengths(arg):
    non_english_letters = re.compile('[^a-zA-Z]')
    return {palindrome for palindrome in re.findall('(?i)(\\\\b[\\\\w]{12,220}\\\\b)', arg[12:123]) if not non_english_letters.search(palindrome)}