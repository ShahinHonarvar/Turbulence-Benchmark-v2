import re

def palindrome_of_length_n(s):
    return set(re.findall('(?i)(?=([^aieouAEIOU][^aieouAEIOU]*[aieouAEIOU]))([aieouAEIOU][^aieouAEIOU]*)\\1', s))