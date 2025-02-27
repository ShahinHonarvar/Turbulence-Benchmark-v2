import re

def palindromes_between_indices(s):
    return set(re.findall('((?P<p>(?P<c>.)+)(?P<q>.))\x01(?P<r>.){7}(?P<s>.){8}(?P=q)\x02(?P=p)', s, flags=re.I))